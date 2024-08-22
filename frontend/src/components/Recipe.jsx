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
            <ul>
                <li className="recipe_list_item"><a rel="nofollow noreferrer" href="https://www.stonefire.com/products/original-mini-naan/">Stonefire Mini Naan Bread(s)</a></li>
                <li className="recipe_list_item">Pizza Sauce</li>
                <li className="recipe_list_item">Pizza Cheese Blend, Shredded</li>
                <li className="recipe_list_item">Mexican Cheese Blend, Shredded</li>
                <li className="recipe_list_item">Pepperoni Slices</li>
            </ul>
            <h2 className="recipe_section_label">Steps</h2>
            <ol>
                <li className="recipe_list_item">Preheat your oven to 450°.</li>
                <li className="recipe_list_item">Prepare an oven-safe tray with aluminum foil coated in cooking spray. Place naan bread(s) on the tray.</li>
                <li className="recipe_list_item">Spread sauce to desired thickness onto naan bread(s).</li>
                <li className="recipe_list_item">Sprinkle pizza cheese blend over sauce until completely covered.</li>
                <li className="recipe_list_item">Place 4-5 pepperoni slices evenly on the cheese layer.</li>
                <li className="recipe_list_item">Sprinkle another layer of pizza cheese blend over the pepperoni.</li>
                <li className="recipe_list_item">Lightly cover the pizza cheese blend with some mexican cheese.</li>
                <li className="recipe_list_item">Place tray in oven and bake until cheese is melted, the naan breads become crispy, or until desired.</li>
            </ol>
        </div>
    )
}