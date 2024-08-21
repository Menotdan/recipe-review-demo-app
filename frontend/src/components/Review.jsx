import { useState } from 'react'

export default function Review({ reviewList, setReviewList, review_id, reviewer_name, review_rating, review_text, review_likes }) {
    function like() {
        reviewList[review_id].likes += 1;
        setReviewList(reviewList);
    }

    return (
        <div id="review">
            <h2 id="reviewer_name">{ reviewer_name }</h2>
            Rating: <b id="review_rating">{ review_rating }/10</b>
            <p id="review_text">{ review_text }</p>
            <button id="like_button" onClick={like}><i id="like_test">{ review_likes }</i> <img id="like_icon" src="assets/like_icon.svg" width={24}></img></button>
        </div>
    )
}