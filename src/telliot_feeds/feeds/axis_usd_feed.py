"""Datafeed for current price of AXIS in USD."""
from telliot_feeds.datafeed import DataFeed
from telliot_feeds.queries.price.spot_price import SpotPrice
from telliot_feeds.sources.price.spot.coingecko import CoinGeckoSpotPriceSource
from telliot_feeds.sources.price_aggregator import PriceAggregator

axis_usd_median_feed = DataFeed(
    query=SpotPrice(asset="axis", currency="usd"),
    source=PriceAggregator(
        asset="axis",
        currency="usd",
        algorithm="median",
        sources=[
            CoinGeckoSpotPriceSource(asset="axis-alive", currency="usd"),
        ],
    ),
)
