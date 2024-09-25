"""Datafeed for current price of INC in USD."""
from telliot_feeds.datafeed import DataFeed
from telliot_feeds.queries.price.spot_price import SpotPrice
from telliot_feeds.sources.price.spot.coingecko import CoinGeckoSpotPriceSource
from telliot_feeds.sources.price.spot.coinpaprika import CoinpaprikaSpotPriceSource
from telliot_feeds.sources.price_aggregator import PriceAggregator

inc_usd_median_feed = DataFeed(
    query=SpotPrice(asset="inc", currency="usd"),
    source=PriceAggregator(
        asset="inc",
        currency="usd",
        algorithm="median",
        sources=[
            CoinGeckoSpotPriceSource(asset="pulsex-incentive-token", currency="usd"),
            CoinpaprikaSpotPriceSource(asset="inc-incentive", currency="usd"),
        ],
    ),
)
