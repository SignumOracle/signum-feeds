"""Datafeed for current price of SPARK in USD."""
from telliot_feeds.datafeed import DataFeed
from telliot_feeds.queries.price.spot_price import SpotPrice
from telliot_feeds.sources.price.spot.coingecko import CoinGeckoSpotPriceSource
from telliot_feeds.sources.price_aggregator import PriceAggregator

spark_usd_median_feed = DataFeed(
    query=SpotPrice(asset="spark", currency="usd"),
    source=PriceAggregator(
        asset="spark",
        currency="usd",
        algorithm="median",
        sources=[
            CoinGeckoSpotPriceSource(asset="sparkswap", currency="usd"),
        ],
    ),
)
