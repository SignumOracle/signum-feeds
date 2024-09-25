"""Datafeed for current price of PAXG in USD."""
from telliot_feeds.datafeed import DataFeed
from telliot_feeds.queries.price.spot_price import SpotPrice
from telliot_feeds.sources.price.spot.coingecko import CoinGeckoSpotPriceSource
from telliot_feeds.sources.price_aggregator import PriceAggregator

paxg_usd_median_feed = DataFeed(
    query=SpotPrice(asset="paxg", currency="usd"),
    source=PriceAggregator(
        asset="paxg",
        currency="usd",
        algorithm="median",
        sources=[
            CoinGeckoSpotPriceSource(asset="pax-gold", currency="usd"),
        ],
    ),
)
