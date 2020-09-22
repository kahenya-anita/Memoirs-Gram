from flask import render_template, request, Blueprint
from app.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return redirect(url_for('main.home'))
    return render_template('home.html', title='Memoirs Gram')


@main.route("/about")
def about():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('about.html', posts=posts)