"""Datafeed for current price of PLSP in USD."""
from telliot_feeds.datafeed import DataFeed
from telliot_feeds.queries.price.spot_price import SpotPrice
from telliot_feeds.sources.price.spot.coingecko import CoinGeckoSpotPriceSource
from telliot_feeds.sources.price_aggregator import PriceAggregator

plsp_usd_median_feed = DataFeed(
    query=SpotPrice(asset="plsp", currency="usd"),
    source=PriceAggregator(
        asset="plsp",
        currency="usd",
        algorithm="median",
        sources=[
            CoinGeckoSpotPriceSource(asset="pulsepot", currency="usd"),
        ],
    ),
)
