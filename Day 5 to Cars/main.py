from typing import List
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session, Product
from schemas import CategoryCreate, CategoryOut, ProductCreate, ProductOut, UserOut, get_db, User, Category, ReviewCreate, ReviewOut, UserCreate, Review, ProductUpdate, Product

@app.post("/user", response_model = UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User (
        full_name = user.full_name,
        email = user.email
    )
    db.add (db_user)
    db.commit ()
    db.refresh (db_user)
    return db_user

@app.post("/categories", response_model = CategoryOut)
def create_category (category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = Category(**category.dict())
    db.add (db_category)
    db.commit ()
    db.refresh (db_category)
    return db_category

@app.post("/product", response_model = ProductOut)
def create_product (product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product (
        title = product.title,
        content = product.content,
        category_id = product.category_id
    )
    db_product.products = db.query(Product).fliter(Product.id.in_(Product.user_ids)).all()
    db.add (db_product)
    db.commit ()
    db.refresh (db_product)
    return db_product

@app.post ("/product", response_model = ProductOut)
def create_product (product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product (
        title = product.title,
        content = product.content,
        category_id = product.category_id
    )
    users = []
    for user_id in user.author_ids:
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            user.append(user)
        db.add (db_product)
        db.commit ()
        db.refresh (db_product)
        return db_product
    
@app.get("/products", response_model = List[ProductOut])
def list_products (db: Session = Depends(get_db)):
    return db.query(Product).all()

@app.post("/products/{product_id}/reviews", response_model = ReviewOut)
def add_review (product_id: int, review: ReviewCreate, db: Session = Depends(get_db)):
    db_product = db.query(Product).get(product_id)
    if not db_product:
        raise HTTPException (status_code = 404, detail = "Статья не найдена")
    db_review = Review(**review.dict(), product_id = product_id)
    db.add (db_review)
    db.commit ()
    db.refresh (db_review)
    return db_review

@app.patch("product/{product_id}", response_model = ProductOut)
def update_product (product_id: int, update_data: ProductUpdate, db: Session = Depends(get_db)):
    db_product = db.query(Product).get(product_id)
    if not db_product:
        raise HTTPException(status_code = 404, detail = "Статья не найдена")
    
    if update_data.title is not None:
        db_product.title = update_data.title
    if update_data.content is not None:
        db_product.content = update_data.content
    if update_data.category_id is not None:
        db_product.category_id = update_data.category_id
    if update_data.user_ids is not None:
        db_product.users = db.query(User).filter(User.id.in_(update_data.user_ids)).all()

    db.commit ()
    db.refresh (db_product)
    return db_product

@app.delete("/reviews/{review_id}", response_model = dict)
def delete_review (review_id: int, db: Session = Depends(get_db)):
    db_review = db.query(Review).get(review_id)
    if not db_review:
        raise HTTPException (status_code = 404, detail = "Отзыв не найден")
    
    db.delete(db_review)
    db.commit()
    return {"message": "Отзыв успешно удалён"}