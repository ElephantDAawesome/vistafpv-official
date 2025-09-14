from main import db, Blog, app
with app.app_context():
    db.create_all()

    firstblog = Blog(
        title ='Week 1',
        headline = 'Southern Monta Vista',
        description = 'Welcome to our first real blog using Flask!',
        footage = 'https://www.youtube.com/embed/hsAOlaBJmco',
        image = '../static/blog1map.png'
        )
    db.session.add_all([firstblog])
    db.session.commit()


# id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.Text)
#     headline = db.Column(db.Text)
#     description = db.Column(db.Text)
#     footage = db.Column(db.Text)