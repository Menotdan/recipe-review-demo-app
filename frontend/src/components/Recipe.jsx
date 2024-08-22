export default function Recipe({ reviewList }) {
    const reviews = Object.values(reviewList);
    const reviewCount = reviews.length;

    let reviewRatings = reviews.reduce((accumulator, review) => {
        return accumulator + review.rating;
    }, 0);

    console.log(reviewRatings);
    console.log(reviewCount);
    console.log(reviews);
    const averageRating = Number.parseFloat(reviewRatings / reviewCount).toFixed(2);

    return (
        <>
            <h1>Simple Homemade Naan Bread Pizza</h1>
            <p>Average Rating: {averageRating}/10</p>
        </>
    )
}