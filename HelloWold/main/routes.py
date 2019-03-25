from flask import render_template, request, Blueprint
from HelloWold.models import Post
main = Blueprint('main', __name__)

#route is to navigate around the webpage
# "/" is the root page of the website
# blueprints separates the methods

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=4)
    return render_template('home.html', posts=posts)

@main.route("/about")
def about():
    return render_template('about.html', title='About')
