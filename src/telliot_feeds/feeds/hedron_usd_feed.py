"""Datafeed for current price of HEDRON in USD."""
from telliot_feeds.datafeed import DataFeed
from telliot_feeds.queries.price.spot_price import SpotPrice
from telliot_feeds.sources.price.spot.coingecko import CoinGeckoSpotPriceSource
from telliot_feeds.sources.price_aggregator import PriceAggregator

hedron_usd_median_feed = DataFeed(
    query=SpotPrice(asset="hedron", currency="usd"),
    source=PriceAggregator(
        asset="hedron",
        currency="usd",
        algorithm="median",
        sources=[
            CoinGeckoSpotPriceSource(asset="hedron", currency="usd"),
        ],
    ),
)
