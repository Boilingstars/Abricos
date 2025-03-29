class AnalyticsRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'GoodsMarketAnalysis':
            return 'goods_analytics_db'
        elif model._meta.app_label == 'BuisnessMarketAnalysis':
            return 'buisness_analytics_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'Users':
            return 'goods_analytics_db'
        elif model._meta.app_label == 'BuisnessMarketAnalysis':
            return 'buisness_analytics_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'Users':
            return db == 'users_manager_db'
        elif model._meta.app_label == 'BuisnessMarketAnalysis':
            return 'buisness_analytics_db'
        return None