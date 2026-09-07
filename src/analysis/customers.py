"""Análisis de clientes."""
def calculate_post_night_purchase(df_check, hours):
    
    condition = (
        (df_check["hours_to_purchase"] > 0) &
        (df_check["hours_to_purchase"] <= hours)
    )
    
    result = (
        df_check
        .assign(
            purchase_after_night=condition
        )
        .groupby("user_id")["purchase_after_night"]
        .any()
    )
    
    return result