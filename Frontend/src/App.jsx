import { Route, Routes } from 'react-router-dom'
import './App.css'
import Landing from './pages/landing/Landing'
import ImageUpload from './pages/image-upload/ImageUpload'
import Results from './pages/results/Results'

function App() 
{
  return (
    <>
      <Routes>
        <Route path="/" element={<Landing/>}/>
        <Route path="/image-upload" element={<ImageUpload/>}/>
        <Route path="/results" element={<Results/>}/>
      </Routes>
    </>
  )
}

export default App
