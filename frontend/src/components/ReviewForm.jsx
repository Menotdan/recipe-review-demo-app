import { useState } from "react";
import './ReviewForm.css'


export default function ReviewForm() {
    const [submitting, setSubmitting] = useState(false);

    function sendReview(event) {
        event.preventDefault();
        if (submitting) return;

        setSubmitting(true);
        const elements = event.target.elements;

        let newReview = {};
        newReview["name"] = elements.name.value;
        newReview["text"] = elements.text.value;
        newReview["rating"] = elements.rating.value;

        setSubmitting(false);
    }

    return (
        <form id="review_form" onSubmit={sendReview}>
            <h2>Leave a review!</h2>
            Your Name: <input id="review_form_name" name="name" /> <br />
            Rating: <input id="review_form_rating" name="rating" type="number" min={0} max={10} /> /10 <br />
            <textarea id="review_form_text" name="text" /> <br />
            <button id="review_form_submit" type="submit">Send Review</button>
        </form>
    )
}