import useSWR from 'swr'
import { motion } from 'framer-motion'
const fetcher = url => fetch(url).then(res => res.json())
export default function NewsCard() {
  const { data } = useSWR(
    `https://newsapi.org/v2/top-headlines?country=it&pageSize=5&apiKey=${process.env.NEXT_PUBLIC_NEWS_API_KEY}`,
    fetcher,
    { refreshInterval: 300000 }
  )
  if (!data) return null
  return (
    <div className="space-y-4">
      {data.articles.map((a, i) => (
        <motion.div key={i} initial={{ x: 100 }} animate={{ x: 0 }} transition={{ delay: i * 0.2 }} className="bg-white p-4 rounded-2xl shadow-md flex">
          {a.urlToImage && <img src={a.urlToImage} className="w-24 h-24 object-cover rounded-lg mr-4" alt="" />}
          <div>
            <h3 className="font-bold">{a.title}</h3>
            <p className="text-sm line-clamp-2">{a.description}</p>
          </div>
        </motion.div>
      ))}
    </div>
  )
}
