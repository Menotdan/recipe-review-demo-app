import { useEffect, useState } from 'react';
import Review from '/components/Review.jsx'

export default function ReviewList({ reviewList, setReviewList }) {
    const [fetchError, setFetchError] = useState(undefined);
    const [fetched, setFetched] = useState(false);

    useEffect(() => {
        const dataFetch = async () => {
            try {
                const response = await fetch(
                    `${import.meta.env.VITE_SERVER_URL}/api/reviews`,
                );

                if (!response.ok) {
                    throw new Error(response.status);
                }

                const data = await response.json();

                let dictData = {};
                data.forEach(review => {
                    dictData[review['id']] = review;
                });

                setReviewList(dictData);
                setFetched(true);
            }
            catch (err) {
                setFetchError(err);
            }
        };

        dataFetch();
    }, []);

    if (fetchError != undefined) {
        return (
            <>
                <h1>Error!</h1>
                <p>{fetchError}</p>
            </>
        )
    }

    if (!fetched) {
        return (
            <>
             <h1>Loading...</h1>
            </>
        )
    }

    return (
        <div>
            {
                Object.values(reviewList).map((review, i) =>
                    <Review
                        key = {review.id}
                        reviewList={reviewList} 
                        setReviewList={setReviewList}
                        review_id = {review.id}
                        reviewer_name = {review.name}
                        review_rating = {review.rating}
                        review_text = {review.text}
                        review_likes = {review.likes}
                    />
                )
            }
        </div>
    )
}
