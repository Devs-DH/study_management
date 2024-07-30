import React from 'react'
import './landing.scss'
import Wave from './wave-component/Wave';

function Landing() {
  // const [page, setPage] = React.useState("1");
  function initialPage() {
    return (
      <div>
        <div className='button-container'>
          <button style={{float:"right"}}>
            Log in
          </button>
        </div>
        <h1>
          Study Management App
        </h1>
        <Wave />
      </div>
    )
  }

  return (
    <>
      {
        initialPage()
      }
    </>
  )

}

export default Landing;