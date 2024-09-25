"""Datafeed for current price of PHEX in USD."""
from telliot_feeds.datafeed import DataFeed
from telliot_feeds.queries.price.spot_price import SpotPrice
from telliot_feeds.sources.price.spot.coingecko import CoinGeckoSpotPriceSource
from telliot_feeds.sources.price_aggregator import PriceAggregator

phex_usd_median_feed = DataFeed(
    query=SpotPrice(asset="phex", currency="usd"),
    source=PriceAggregator(
        asset="phex",
        currency="usd",
        algorithm="median",
        sources=[
            CoinGeckoSpotPriceSource(asset="hex-pulsechain", currency="usd"),
        ],
    ),
)
