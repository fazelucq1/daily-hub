import WeatherCard from '../components/WeatherCard'
import NewsCard from '../components/NewsCard'
export default function Home() {
  return (
    <div className="min-h-screen bg-gray-50 p-6 grid grid-cols-1 md:grid-cols-2 gap-6">
      <WeatherCard />
      <NewsCard />
    </div>
  )
}
