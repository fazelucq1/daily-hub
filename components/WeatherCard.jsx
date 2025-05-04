import useSWR from 'swr'
import { motion } from 'framer-motion'
const fetcher = url => fetch(url).then(res => res.json())
export default function WeatherCard() {
  const { data } = useSWR(
    `https://api.openweathermap.org/data/2.5/weather?q=Rome&units=metric&appid=${process.env.NEXT_PUBLIC_WEATHER_API_KEY}`,
    fetcher,
    { refreshInterval: 600000 }
  )
  if (!data) return null
  const { main, weather, name } = data
  return (
    <motion.div animate={{ opacity: [0, 1] }} transition={{ duration: 1 }} className="bg-blue-100 p-4 rounded-2xl shadow-md">
      <h2 className="text-xl font-bold">{name}</h2>
      <div className="flex items-center">
        <img src={`https://openweathermap.org/img/wn/${weather[0].icon}@2x.png`} alt="" />
        <div>
          <p className="text-4xl font-semibold">{Math.round(main.temp)}°C</p>
          <p className="capitalize">{weather[0].description}</p>
        </div>
      </div>
    </motion.div>
  )
}
