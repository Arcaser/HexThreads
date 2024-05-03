import { useState } from 'react'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import './App.css'
import Landing from './pages/landing/Landing'
import ImageUpload from './pages/image-upload/ImageUpload'
import ColorPicker from './pages/color-picker/ColorPicker'

function App() 
{
  return (
    <>
      <Routes>
        <Route path="/" element={<Landing/>}/>
        <Route path="/image-upload" element={<ImageUpload/>}/>
        <Route path="/color-picker'" element={<ColorPicker/>}/>
      </Routes>
    </>
  )
}

export default App
