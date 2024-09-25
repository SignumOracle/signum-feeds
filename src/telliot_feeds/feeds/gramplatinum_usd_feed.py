"""Datafeed for current price of GRAM PLATINUM in USD."""
from telliot_feeds.datafeed import DataFeed
from telliot_feeds.queries.price.spot_price import SpotPrice
from telliot_feeds.sources.price.spot.coingecko import CoinGeckoSpotPriceSource
from telliot_feeds.sources.price_aggregator import PriceAggregator

gramplatinum_usd_median_feed = DataFeed(
    query=SpotPrice(asset="gramplatinum", currency="usd"),
    source=PriceAggregator(
        asset="gramplatinum",
        currency="usd",
        algorithm="median",
        sources=[
            CoinGeckoSpotPriceSource(asset="gram-platinum", currency="usd"),
        ],
    ),
)
