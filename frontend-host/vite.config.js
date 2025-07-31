import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// URL pública del backend en Render (ajusta después del deploy real)
const backendUrl = process.env.VITE_BACKEND_URL || 'http://localhost:5000'

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      // Redirige todas las solicitudes que empiecen con /api al backend
      '/api': {
        target: backendUrl,
        changeOrigin: true,
        secure: false
      }
    }
  }
})

