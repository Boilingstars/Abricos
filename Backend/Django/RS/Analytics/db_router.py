class AnalyticsRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'Analytics':
            if model.__name__ == 'GoodsMarketAnalysis':
                return 'goods_analytics_db'
            elif model.__name__ == 'BuisnessMarketAnalysis':
                return 'buisness_analytics_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'Analytics':
            if model.__name__ == 'GoodsMarketAnalysis':
                return 'goods_analytics_db'
            elif model.__name__ == 'BuisnessMarketAnalysis':
                return 'buisness_analytics_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'Analytics':
            if model_name == 'goodsmarketanalysis':
                return db == 'goods_analytics_db'
            elif model_name == 'buisnessmarketanalysis':
                return db == 'buisness_analytics_db'
        return None