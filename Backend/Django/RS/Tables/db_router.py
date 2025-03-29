class GoodsRouter:
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Определяет, в какую базу данных выполнять миграции."""
        if app_label == 'Tables':
            return db == 'goods_manager_db'  # Выполняйте миграции для приложения Tables во второй базе данных
        return None