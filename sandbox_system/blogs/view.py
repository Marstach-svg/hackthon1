from flask import Blueprint,render_template, url_for, redirect, abort, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from sandbox_system import db
from sandbox_system.models import Blog, BlogCategory
from sandbox_system.blogs.form import BlogForm, BlogSearchForm, BlogCategoryForm
from sandbox_system.blogs.image import add_image

blogs = Blueprint('blogs', __name__)

@blogs.route('/blog_list', methods=['GET', 'POST'])
def blog_list():
    form = BlogSearchForm()
    category_form = BlogCategoryForm()
    if category_form.validate_on_submit():
        new_category = BlogCategory(category=category_form.category.data)
        db.session.add(new_category)
        db.session.commit()
        flash('カテゴリが追加されました')
        return redirect(url_for('blogs.blog_list'))
    blog_categories = BlogCategory.query.order_by(BlogCategory.id.asc()).all()
    page = request.args.get('page', 1, type=int)
    blogs = Blog.query.order_by(Blog.id.desc()).paginate(page=page, per_page=10)
    return render_template('blog/blog_list.html', form=form, blog_categories=blog_categories, blogs=blogs, category_form=category_form)

@blogs.route('/blog_create', methods=['GET', 'POST'])
@login_required
def blog_create():
    form = BlogForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture = add_image(form.picture.data)
        else:
            picture = ''
        blog = Blog(title=form.title.data, summary=form.summary.data, text=form.text.data, image=picture, user_id=current_user.id, category_id=form.category.data)
        db.session.add(blog)
        db.session.commit()
        flash('ブログを投稿しました')
        return redirect(url_for('blogs.blog_list'))
    return render_template('blog/blog_create.html', form=form)

@blogs.route('/<int:blog_id>/blog')
def blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    form = BlogSearchForm()
    blog_categories = BlogCategory.query.order_by(BlogCategory.id.asc()).all()
    return render_template('blog/blog.html', blog=blog, form=form, blog_categories=blog_categories)

@blogs.route('/search', methods=['GET', 'POST'])
def search():
    form = BlogSearchForm()
    category_form = BlogCategoryForm()
    searchtext = ''
    if form.validate_on_submit():
        searchtext = form.searchtext.data
    elif request.method == 'GET':
        form.searchtext.data == ''
    #ブログ記事の取得
    page = request.args.get('page', 1, type=int)
    blogs = Blog.query.filter((Blog.text.contains(searchtext)) | (Blog.title.contains(searchtext)) | (Blog.summary.contains(searchtext))).order_by(Blog.id.desc()).paginate(page=page, per_page=10)
    #カテゴリの取得
    blog_categories = BlogCategory.query.order_by(BlogCategory.id.asc()).all()
    return render_template('blog/blog_list.html', blogs=blogs, blog_categories=blog_categories, form=form, category_form=category_form, searchtext=searchtext)

@blogs.route('/<int:blog_category_id>/category_blog', methods=['GET', 'POST'])
def category_blog(blog_category_id):
    form = BlogSearchForm()
    category_form = BlogCategoryForm()
    blog_category = BlogCategory.query.filter_by(id=blog_category_id).first()
    page = request.args.get('page', 1, type=int)
    blogs = Blog.query.filter_by(category_id=blog_category_id).order_by(Blog.id.desc()).paginate(page=page, per_page=10)
    #カテゴリの取得
    blog_categories = BlogCategory.query.order_by(BlogCategory.id.asc()).all()
    return render_template('blog/blog_list.html', blogs=blogs, blog_categories=blog_categories, form=form, category_form=category_form, blog_category=blog_category)

@blogs.route('/<int:user_id>/user_blog', methods=['GET', 'POST'])
def user_blog(user_id):
    form = BlogSearchForm()
    category_form = BlogCategoryForm()
    blog_user = Blog.query.filter_by(user_id=user_id).first()
    page = request.args.get('page', 1, type=int)
    blogs = Blog.query.filter_by(user_id=user_id).order_by(Blog.id.desc()).paginate(page=page, per_page=10)
    #カテゴリの取得
    blog_categories = BlogCategory.query.order_by(BlogCategory.id.asc()).all()
    return render_template('blog/blog_list.html', blogs=blogs, blog_categories=blog_categories, form=form, category_form=category_form, blog_user=blog_user)

@blogs.route('/blog_maintenance')
@login_required
def blog_maintenance():
    if not current_user.is_administrator():
        abort(403)
    page = request.args.get('page', 1, type=int)
    blogs = Blog.query.order_by(Blog.id).paginate(page=page, per_page=10)
    return render_template('maintenance/blog_maintenance.html', blogs=blogs)