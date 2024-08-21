import { useState } from 'react'
import './App.css'
import ReviewList from '/components/ReviewList.jsx'
import ReviewForm from '/components/ReviewForm.jsx'

function App() {
  return (
    <>
      <ReviewForm />
      <ReviewList />
    </>
  )
}

export default App