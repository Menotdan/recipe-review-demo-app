import { useState } from "react";
import './ReviewForm.css'


export default function ReviewForm({ reviewList, setReviewList }) {
    const [submitting, setSubmitting] = useState(false);

    function sendReview(event) {
        event.preventDefault();
        if (submitting) return;

        setSubmitting(true);
        const elements = event.target.elements;

        let newReview = {};
        newReview["name"] = elements.name.value;
        newReview["text"] = elements.text.value;
        newReview["rating"] = Number.parseInt(elements.rating.value);

        fetch(`${import.meta.env.VITE_SERVER_URL}/api/reviews/create`, {
            method: "POST",
            body: JSON.stringify(newReview),
            headers: {
                "Content-Type": "application/json",
            },
        }).then((response) => {
            if (response.ok) {
                response.json().then((id) => {
                    newReview["likes"] = 0;
                    newReview["id"] = id;

                    let reviewListClone = { ...reviewList }
                    reviewListClone[id] = newReview;
                    setReviewList(reviewListClone);

                    elements.name.value = "";
                    elements.text.value = "";
                    elements.rating.value = 0;
                    setSubmitting(false);
                }).catch((err) => {
                    console.error(err);
                    setSubmitting(false);
                });
            }
            else {
                console.error(`Post failed, status code: ${response.status}`);
                setSubmitting(false);
            }
        }).catch((err) => {
            console.error(err);
            setSubmitting(false);
        });
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