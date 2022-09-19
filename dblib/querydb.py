from databricks import sql
import os

def querydb(query="SELECT player, win_loss_pct,mp_per_g, fg3a_per_g FROM default.nba_dataset ORDER BY win_loss_pct DESC LIMIT 5"):
    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN")) as connection:

        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        
            for row in result:
                print(row)

    return result