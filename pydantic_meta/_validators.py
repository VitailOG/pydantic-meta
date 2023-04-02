def validate_intersection_between_config_and_attr_class(config, kwargs):
    if set(dir(config)) & set(kwargs):
        raise TypeError(
            "Specifying config in two places is ambiguous, use either Config attribute or class kwargs"
        )
