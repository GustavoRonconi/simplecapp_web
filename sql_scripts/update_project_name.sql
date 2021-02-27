UPDATE django_migrations
   SET app = 'api'
 WHERE app = 'app_simpleCapp';

UPDATE django_content_type
   SET app_label = 'api'
 WHERE app_label = 'app_simpleCapp';