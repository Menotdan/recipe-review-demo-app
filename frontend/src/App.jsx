import { useState } from 'react'
import './App.css'
import ReviewList from '/components/ReviewList.jsx'

const SERVER_URL = 'http://localhost:8000';

function App() {
  return (
    <>
      <ReviewList />
    </>
  )
}

export default App