import requests
from flask import Blueprint, jsonify, request
from .. import db
from .models import User, UserTrash, Photo, PhotoTrash, Post, PostTrash, Comment, \
    CommentTrash, Todo, TodoTrash, Album, AlbumTrash

api = Blueprint('api', __name__)


# POSTS
@api.route('/posts/')
def get_posts():
    posts = Post.query.all()
    return jsonify([post.to_json() for post in posts]), 200


@api.route('/posts/<int:id>')
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify(post.to_json()), 200


@api.route('/users/<int:id>/posts')
def get_posts_of_an_user(id):
    posts = Post.query.filter_by(userId=id).all()
    return jsonify([post.to_json() for post in posts]), 200


@api.route('/posts/', methods=['POST'])
def new_post():
    data = request.get_json()

    post = Post(userId=data['userId'],
                id=data['id'],
                title=data['title'],
                body=data['body']
                )
    db.session.add(post)
    db.session.commit()
    return jsonify({'userId': post.userId,
                    'id': post.id,
                    'title': post.title,
                    'body': post.body
                    }), 201


@api.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    post = Post.query.get_or_404(id)
    post.title = request.json.get('title', post.title)
    post.body = request.json.get('body', post.body)
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_json()), 204


@api.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = Post.query.filter_by(id=id).first_or_404()
    post_trash = PostTrash(
        userId=post.userId,
        id=post.id,
        title=post.title,
        body=post.body
    )
    db.session.add(post_trash)
    db.session.commit()

    # deleting post
    db.session.delete(post)
    db.session.commit()
    return {
        'success': 'post deleted successfully'
    }


# Displaying the trash for posts
@api.route('/posts_trash/')
def get_post_trash():
    posts = PostTrash.query.all()
    return jsonify([post.to_json() for post in posts]), 200


# Restoring post
@api.route('/posts_restore/<int:id>', methods=['DELETE'])
def restore_post(id):
    post = PostTrash.query.filter_by(id=id).first_or_404()
    post_restore = Post(
        userId=post.userId,
        id=post.id,
        title=post.title,
        body=post.body
    )
    db.session.add(post_restore)
    db.session.commit()

    # deleting post
    db.session.delete(post)
    db.session.commit()
    return {
        'success': 'post restored successfully'
    }


# COMMENTS
@api.route('/comments/')
def get_comments():
    comments = Comment.query.all()
    return jsonify([comment.to_json() for comment in comments])


@api.route('/comments/<int:id>')
def get_comment(id):
    comment = Comment.query.get_or_404(id)
    return jsonify(comment.to_json())


@api.route('/posts/<int:id>/comments')
def get_comments_of_a_post(id):
    comments = Comment.query.filter_by(postId=id).all()
    return jsonify([comment.to_json() for comment in comments])


@api.route('/comments/', methods=['POST'])
def new_comment():
    data = request.get_json()

    comment = Comment(postId=data['postId'],
                      id=data['id'],
                      name=data['name'],
                      email=data['email'],
                      body=data['body']
                      )
    db.session.add(comment)
    db.session.commit()
    return jsonify({'postId': comment.postId,
                    'id': comment.id,
                    'name': comment.name,
                    'email': comment.email,
                    'body': comment.body
                    }), 201


@api.route('/comments/<int:id>', methods=['PUT'])
def update_comment(id):
    comment = Comment.query.get_or_404(id)
    comment.name = request.json.get('name', comment.name)
    comment.email = request.json.get('email', comment.email)
    comment.body = request.json.get('body', comment.body)
    db.session.add(comment)
    db.session.commit()
    return jsonify(comment.to_json())


@api.route('/comments/<int:id>', methods=['DELETE'])
def delete_comment(id):
    comment = Comment.query.filter_by(id=id).first_or_404()
    comment_trash = CommentTrash(
        postId=comment.postId,
        id=comment.id,
        name=comment.name,
        email=comment.email,
        body=comment.body
    )
    db.session.add(comment_trash)
    db.session.commit()

    # deleting comment
    db.session.delete(comment)
    db.session.commit()
    return {
        'success': 'comment deleted successfully'
    }


# Displaying the trash for posts
@api.route('/comments_trash/')
def get_comment_trash():
    comments = CommentTrash.query.all()
    return jsonify([comment.to_json() for comment in comments]), 200


# Restoring comment
@api.route('/comments_restore/<int:id>', methods=['DELETE'])
def restore_comment(id):
    comment = CommentTrash.query.filter_by(id=id).first_or_404()
    comment_restore = Comment(
        postId=comment.postId,
        id=comment.id,
        name=comment.name,
        email=comment.email,
        body=comment.body
    )
    db.session.add(comment_restore)
    db.session.commit()

    # deleting comment
    db.session.delete(comment)
    db.session.commit()
    return {
        'success': 'comment restored successfully'
    }


# ALBUM
@api.route('/albums/')
def get_albums():
    albums = Album.query.all()
    return jsonify([album.to_json() for album in albums])


@api.route('/albums/<int:id>')
def get_album(id):
    album = Album.query.get_or_404(id)
    return jsonify(album.to_json())


@api.route('/users/<int:id>/albums')
def get_albums_of_an_user(id):
    albums = Album.query.filter_by(userId=id).all()
    return jsonify([album.to_json() for album in albums])


@api.route('/albums/', methods=['POST'])
def new_album():
    data = request.get_json()

    album = Album(userId=data['userId'],
                  id=data['id'],
                  title=data['title']
                  )
    db.session.add(album)
    db.session.commit()
    return jsonify({'userId': album.userId,
                    'id': album.id,
                    'title': album.title,
                    }), 201


@api.route('/albums/<int:id>', methods=['PUT'])
def update_albums(id):
    album = Album.query.get_or_404(id)
    album.title = request.json.get('title', album.title)
    # No other field to modify
    db.session.add(album)
    db.session.commit()
    return jsonify(album.to_json())


@api.route('/albums/<int:id>', methods=['DELETE'])
def delete_album(id):
    album = Album.query.filter_by(id=id).first_or_404()
    album_trash = AlbumTrash(
        userId=album.userId,
        id=album.id,
        title=album.title
    )
    db.session.add(album_trash)
    db.session.commit()

    # deleting post
    db.session.delete(album)
    db.session.commit()
    return {
        'success': 'album deleted successfully'
    }


# Displaying the trash for albums
@api.route('/albums_trash/')
def get_album_trash():
    albums = AlbumTrash.query.all()
    return jsonify([album.to_json() for album in albums]), 200


# Restoring post
@api.route('/albums_restore/<int:id>', methods=['DELETE'])
def restore_album(id):
    album = AlbumTrash.query.filter_by(id=id).first_or_404()
    album_restore = Album(
        userId=album.userId,
        id=album.id,
        title=album.title
    )
    db.session.add(album_restore)
    db.session.commit()

    # deleting post
    db.session.delete(album)
    db.session.commit()
    return {
        'success': 'album restored successfully'
    }


# PHOTOS
@api.route('/photos/')
def get_photos():
    photos = Photo.query.all()
    return jsonify([photo.to_json() for photo in photos])


@api.route('/photos/<int:id>')
def get_photo(id):
    photo = Photo.query.get_or_404(id)
    return jsonify(photo.to_json())


@api.route('/albums/<int:id>/photos')
def get_photos_of_an_album(id):
    photos = Photo.query.filter_by(albumId=id).all()
    return jsonify([photo.to_json() for photo in photos])


@api.route('/photos/', methods=['POST'])
def new_photo():
    data = request.get_json()

    photo = Photo(albumId=data['albumId'],
                  id=data['id'],
                  title=data['title'],
                  url=data['url'],
                  thumbnailUrl=data['thumbnailUrl']
                  )
    db.session.add(photo)
    db.session.commit()
    return jsonify({'albumId': photo.albumId,
                    'id': photo.id,
                    'title': photo.title,
                    'url': photo.url,
                    'thumbnailUrl': photo.thumbnailUrl
                    }), 201


@api.route('/photos/<int:id>', methods=['PUT'])
def update_photos(id):
    photo = Photo.query.get_or_404(id)
    photo.title = request.json.get('title', photo.title)
    photo.url = request.json.get('url', photo.url)
    photo.thumbnailUrl = request.json.get('thumbnailUrl', photo.thumbnailUrl)

    db.session.add(photo)
    db.session.commit()
    return jsonify(photo.to_json())


@api.route('/photos/<int:id>', methods=['DELETE'])
def delete_photos(id):
    photo = Photo.query.filter_by(id=id).first_or_404()
    photo_trash = PhotoTrash(
        albumId=photo.albumId,
        id=photo.id,
        title=photo.title,
        url=photo.url,
        thumbnailUrl=photo.thumbnailUrl
    )
    db.session.add(photo_trash)
    db.session.commit()

    # deleting post
    db.session.delete(photo)
    db.session.commit()
    return {
        'success': 'photo deleted successfully'
    }


# Displaying the trash for photo
@api.route('/photos_trash/')
def get_photo_trash():
    photos = PhotoTrash.query.all()
    return jsonify([photo.to_json() for photo in photos]), 200


# Restoring photo
@api.route('/photo_restore/<int:id>', methods=['DELETE'])
def restore_photo(id):
    photo = PhotoTrash.query.filter_by(id=id).first_or_404()
    photo_restore = Post(
        albumId=photo.albumId,
        id=photo.id,
        title=photo.title,
        url=photo.url,
        thumbnailUrl=photo.thumbnailUrl
    )
    db.session.add(photo_restore)
    db.session.commit()

    # deleting post
    db.session.delete(photo)
    db.session.commit()
    return {
        'success': 'photo restored successfully'
    }


# TODOS
@api.route('/todos/')
def get_todos():
    todos = Todo.query.all()
    return jsonify([todo.to_json() for todo in todos])


@api.route('/todos/<int:id>')
def get_todo(id):
    todo = Todo.query.get_or_404(id)
    return jsonify(todo.to_json())


@api.route('/users/<int:id>/todos')
def get_todos_of_an_user(id):
    todos = Todo.query.filter_by(userId=id).all()
    return jsonify([todo.to_json() for todo in todos])


@api.route('/todos/', methods=['POST'])
def new_todo():
    data = request.get_json()

    todo = Todo(userId=data['userId'],
                id=data['id'],
                title=data['title']
                )
    db.session.add(todo)
    db.session.commit()
    return jsonify({'userId': todo.userId,
                    'id': todo.id,
                    'title': todo.title,
                    }), 201


@api.route('/todos/<int:id>', methods=['PUT'])
def update_todos(id):
    todo = Todo.query.get_or_404(id)
    todo.title = request.json.get('title', todo.title)
    # No other field to modify
    db.session.add(todo)
    db.session.commit()
    return jsonify(todo.to_json())


@api.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = Todo.query.filter_by(id=id).first_or_404()
    todo_trash = TodoTrash(
        userId=todo.userId,
        id=todo.id,
        title=todo.title,
    )
    db.session.add(todo_trash)
    db.session.commit()

    # deleting post
    db.session.delete(todo)
    db.session.commit()
    return {
        'success': 'todo deleted successfully'
    }


# Displaying the trash for todos
@api.route('/todos_trash/')
def get_todo_trash():
    todos = TodoTrash.query.all()
    return jsonify([todo.to_json() for todo in todos]), 200


@api.route('/todos_restore/<int:id>', methods=['DELETE'])
def restore_todo(id):
    todo = TodoTrash.query.filter_by(id=id).first_or_404()
    todo_restore = Todo(
        userId=todo.userId,
        id=todo.id,
        title=todo.title,
    )
    db.session.add(todo_restore)
    db.session.commit()

    db.session.delete(todo)
    db.session.commit()
    return {
        'success': 'todo restored successfully'
    }


##### **** Filling data from the API into the database **** #####
class Myapi:
    def get_item(self, item):
        url = 'https://jsonplaceholder.typicode.com/{}'.format(item)
        results = requests.get(url)
        return results.json()


items = ['users', 'posts', 'comments', 'albums', 'photos', 'todos']


def fill_users():
    if User.query.count() == 0:
        users = Myapi().get_item(items[0])  # all users from the API
        for i in range(len(users)):
            one_user = users[i]

            address = one_user['address']
            geo = address['geo']
            company = one_user['company']

            user = User(id=one_user['id'], # .replace(11+i) and all over the others rows
                        name=one_user['name'],
                        username=one_user['username'],
                        email=one_user['email'],
                        street=address['street'],
                        suite=address['suite'],
                        city=address['city'],
                        zipcode=address['zipcode'],
                        lat=geo['lat'],
                        lng=geo['lng'],
                        phone=one_user['phone'],
                        website=one_user['website'],
                        company_name=company['name'],
                        company_catchPhrase=company['catchPhrase'],
                        company_bs=company['bs']
                        )

            db.session.add(user)
            db.session.commit()


def fill_posts():
    if Post.query.count() == 0:
        posts = Myapi().get_item(items[1])  # all posts
        for i in range(len(posts)):
            one_post = posts[i]

            post = Post(userId=one_post['userId'],
                        id=one_post['id'],
                        title=one_post['title'],
                        body=one_post['body']
                        )

            db.session.add(post)
            db.session.commit()


def fill_comments():
    if Comment.query.count() == 0:
        comments = Myapi().get_item(items[2])  # all comments
        for i in range(len(comments)):
            one_comment = comments[i]

            comment = Comment(postId=one_comment['postId'],
                              id=one_comment['id'],
                              name=one_comment['name'],
                              email=one_comment['email'],
                              body=one_comment['body']
                              )

            db.session.add(comment)
            db.session.commit()


def fill_albums():
    if Album.query.count() == 0:
        albums = Myapi().get_item(items[3])  # all albums
        for i in range(len(albums)):
            one_album = albums[i]

            album = Album(userId=one_album['userId'],
                          id=one_album['id'],
                          title=one_album['title']
                          )

            db.session.add(album)
            db.session.commit()


def fill_photos():
    if Photo.query.count() == 0:
        photos = Myapi().get_item(items[4])  # all photos
        for i in range(len(photos)):
            one_photo = photos[i]

            photo = Photo(albumId=one_photo['albumId'],
                          id=one_photo['id'],
                          title=one_photo['title'],
                          url=one_photo['url'],
                          thumbnailUrl=one_photo['thumbnailUrl']
                          )

            db.session.add(photo)
            db.session.commit()


def fill_todos():
    if Todo.query.count() == 0:
        todos = Myapi().get_item(items[5])  # all todos
        for i in range(len(todos)):
            one_todo = todos[i]

            todo = Todo(userId=one_todo['userId'],
                        id=one_todo['id'],
                        title=one_todo['title']
                        # completed=one_todo['completed']
                        )

            db.session.add(todo)
            db.session.commit()

# fill_users()
# fill_posts()
# fill_comments()
# fill_albums()
# fill_photos()
# fill_todos()
