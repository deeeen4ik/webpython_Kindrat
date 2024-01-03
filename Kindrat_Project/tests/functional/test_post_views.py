from flask import url_for

def test_all_posts_page_loads(client):
    response = client.get(url_for('post_blp.posts'))
    assert response.status_code == 200
    
    
def test_post_create_page_loads(client, log_in_default_user):
    response = client.get(url_for('post_blp.create_post'))
    assert response.status_code == 200
    assert u'Add Post' in response.data.decode("utf8")
    
    
def test_post_by_id_page_loads(client, init_database):
    response = client.get(url_for('post_blp.view_post', id=1))
    assert response.status_code == 200
    assert b'Created:' in response.data
    
    
def test_post_edit_page_loads(client, init_database, log_in_default_user):
    response = client.get(url_for('post_blp.update_post', id=1))
    assert response.status_code == 200
    assert u'Update Post' in response.data.decode("utf8")