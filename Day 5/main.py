from typing import List
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session, Article
from schemas import CategoryCreate, CategoryOut, ArticleCreate, ArticleOut, AuthorOut, get_db, Author, Category, ReviewCreate, ReviewOut, AuthorCreate, Review, ArticleUpdate, 

@app.post("/authors", response_model = AuthorOut)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    db_author = Author (
        full_name = author.full_name,
        email = author.email
    )
    db.add (db_author)
    db.commit ()
    db.refresh (db_author)
    return db_author

@app.post("/categories", response_model = CategoryOut)
def create_category (category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = Category(**category.dict())
    db.add (db_category)
    db.commit ()
    db.refresh (db_category)
    return db_category

@app.post("/articles", response_model = ArticleOut)
def create_article (article: ArticleCreate, db: Session = Depends(get_db)):
    db_article = Article (
        title = article.title,
        content = article.content,
        category_id = article.category_id
    )
    db_article.authors = db.query(Author).fliter(Author.id.in_(article.author_ids)).all()
    db.add (db_article)
    db.commit ()
    db.refresh (db_article)
    return db_article

@app.post ("/articles", respone_model = ArticleOut)
def create_article (article: ArticleCreate, db: Session = Depends(get_db)):
    db_article = Article (
        title = article.title,
        content = article.content,
        category_id = article.category_id
    )
    authors = []
    for author_id in article.author_ids:
        author = db.query(Author).filter(Author.id == author_id).first()
        if author:
            authors.append(author)
        db.add (db_article)
        db.commit ()
        db.refresh (db_article)
        return db_article
    
@app.get("/articles", respone_model = List[ArticleOut])
def list_articles (db: Session = Depends(get_db)):
    return db.query(Article).all()

@app.post("/articles/{article_id}/reviews", response_model = ReviewOut)
def add_review (article_id: int, review: ReviewCreate, db: Session = Depends(get_db)):
    db_article = db.query(Article).get(article_id)
    if not db_article:
        raise HTTPException (status_code = 404, detail = "Статья не найдена")
    db_review = Review(**review.dict(), article_id = article_id)
    db.add (db_review)
    db.commit ()
    db.refresh (db_review)
    return db_review

@app.patch("articles/{article_id}", response_model = ArticleOut)
def update_article (article_id: int, update_data: ArticleUpdate, db: Session = Depends(get_db)):
    db_article = db.query(Article).get(article_id)
    if not db_article:
        raise HTTPException(status_code = 404, detail = "Статья не найдена")
    
    if update_data.title is not None:
        db_article.title = update_data.title
    if update_data.content is not None:
        db_article.content = update_data.content
    if update_data.category_id is not None:
        db_article.category_id = update_data.category_id
    if update_data.author_ids is not None:
        db_article.authors = db.query(Author).filter(Author.id.in_(update_data.author_ids)).all()

    db.commit ()
    db.refresh (db_article)
    return db_article

@app.delete("/reviews/{review_id}", response_model = dict)
def delete_review (review_id: int, db: Session = Depends(get_db)):
    db_review = db.query(Review).get(review_id)
    if not db_review:
        raise HTTPException (status_code = 404, detail = "Отзыв не найден")
    
    db.delete(db_review)
    db.commit()
    return {"message": "Отзыв успешно удалён"}