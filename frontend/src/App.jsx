import { useState } from 'react'
import './App.css'
import ReviewList from '/components/ReviewList.jsx'
import ReviewForm from '/components/ReviewForm.jsx'
import Recipe from '/components/Recipe.jsx'

function App() {
  const [reviewList, setReviewList] = useState({});

  return (
    <>
      <Recipe
        reviewList={reviewList}
      />
      <ReviewForm
        reviewList={reviewList}
        setReviewList={setReviewList}
      />
      <ReviewList
        reviewList={reviewList}
        setReviewList={setReviewList}
      />
    </>
  )
}

export default App