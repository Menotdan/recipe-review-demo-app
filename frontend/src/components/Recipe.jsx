import './Recipe.css'

export default function Recipe({ reviewList }) {
    const reviews = Object.values(reviewList);
    const reviewCount = reviews.length;

    let reviewRatings = reviews.reduce((accumulator, review) => {
        return accumulator + review.rating;
    }, 0);

    const averageRating = reviewCount > 0 ?
        Number.parseFloat(reviewRatings / reviewCount).toFixed(2)
        : "?";

    return (
        <div id="recipe">
            <h1>Simple Homemade Naan Bread Pizza</h1>
            <p>Average Rating: {averageRating}/10</p>
            <h2 className="recipe_section_label">Ingredients</h2>
            <ul className="recipe_list">
                <li><a rel="nofollow noreferrer" href="https://www.stonefire.com/products/original-mini-naan/">Stonefire Mini Naan Bread(s)</a></li>
                <li>Pizza Sauce</li>
                <li>Pizza Cheese Blend, Shredded</li>
                <li>Mexican Cheese Blend, Shredded</li>
                <li>Pepperoni Slices</li>
            </ul>
            <h2 className="recipe_section_label">Steps</h2>
            <ol className="recipe_list">
                <li>Preheat your oven to 450°.</li>
                <li>Prepare an oven-safe tray with aluminum foil coated in cooking spray. Place naan bread(s) on the tray.</li>
                <li>Spread sauce to desired thickness onto naan bread(s).</li>
                <li>Sprinkle pizza cheese blend over sauce until completely covered.</li>
                <li>Place 4-5 pepperoni slices evenly on the cheese layer.</li>
                <li>Sprinkle another layer of pizza cheese blend over the pepperoni.</li>
                <li>Lightly cover the pizza cheese blend with some mexican cheese.</li>
                <li>Place tray in oven and bake until cheese is melted, the naan breads become crispy, or until desired.</li>
            </ol>
        </div>
    )
}