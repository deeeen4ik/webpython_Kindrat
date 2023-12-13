from flask import flash, redirect, render_template, url_for
from app import db, navigation
from .forms import FeedbackForm
from .models import Feedback
from . import feedback

@feedback.context_processor
def inject_navigation():
    return dict(navigation=navigation())

@feedback.route('/feedbacks', methods=['GET', 'POST'])
def feedbacks():
    feedback_form = FeedbackForm()
    if feedback_form.validate_on_submit():
        username = feedback_form.username.data
        feedback_text = feedback_form.feedback.data

        new_feedback = Feedback(username=username, feedback=feedback_text)
        db.session.add(new_feedback)
        db.session.commit()
        flash('Feedback submitted successfully!', 'success')
        return redirect(url_for('feedback.feedbacks'))

    feedbacks = Feedback.query.all()
    return render_template('feedbacks.html', feedback_form=feedback_form, feedbacks=feedbacks)