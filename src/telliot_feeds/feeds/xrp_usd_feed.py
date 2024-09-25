"""Datafeed for current price of XRP in USD."""
from telliot_feeds.datafeed import DataFeed
from telliot_feeds.queries.price.spot_price import SpotPrice
from telliot_feeds.sources.price.spot.coingecko import CoinGeckoSpotPriceSource
from telliot_feeds.sources.price_aggregator import PriceAggregator

xrp_usd_median_feed = DataFeed(
    query=SpotPrice(asset="xrp", currency="usd"),
    source=PriceAggregator(
        asset="xrp",
        currency="usd",
        algorithm="median",
        sources=[
            CoinGeckoSpotPriceSource(asset="ripple", currency="usd"),
        ],
    ),
)
