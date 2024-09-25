"""Datafeed for current price of HEX in USD."""
from telliot_feeds.datafeed import DataFeed
from telliot_feeds.queries.price.spot_price import SpotPrice
from telliot_feeds.sources.price.spot.coingecko import CoinGeckoSpotPriceSource
from telliot_feeds.sources.price_aggregator import PriceAggregator

hex_usd_median_feed = DataFeed(
    query=SpotPrice(asset="hex", currency="usd"),
    source=PriceAggregator(
        asset="hex",
        currency="usd",
        algorithm="median",
        sources=[
            CoinGeckoSpotPriceSource(asset="hex", currency="usd"),
        ],
    ),
)
