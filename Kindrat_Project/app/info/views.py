from flask import make_response, render_template, request, redirect, url_for, session, flash
from flask_login import login_required
from . import info


@info.route('/info', methods=['GET', 'POST'])
@login_required
def infos():
    username = session.get('username')

    if request.method == 'POST':
        key = request.form.get('key')
        value = request.form.get('value')
        expiry = request.form.get('expiry')

        if key and value:
            response = make_response(redirect(url_for('info.info')))
            response.set_cookie(key, value, expires=expiry)
            flash('Cookie added successfully!', 'success')
            return response
        else:
            flash('Key and value are required to add a cookie', 'error')
            return "Key and value are required to add a cookie"

    delete_key = request.args.get('delete_key')
    if delete_key:
        response = make_response(redirect(url_for('info.info')))
        if delete_key == 'all':
            for key in request.cookies:
                response.delete_cookie(key)
        else:
            response.delete_cookie(delete_key)
        flash('Cookie deleted successfully!', 'success')
        return response

    cookies_info = [(key, request.cookies[key]) for key in request.cookies]
    return render_template('info.html', username=username, cookies_info=cookies_info)