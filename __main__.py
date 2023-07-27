
import pulumi
import pulumi_snowflake as snowflake

# Create a warehouse
warehouse = snowflake.Warehouse(
    'test-warehouse', comment='this is a comment', warehouse_size='x-small')

# Create a role
role = snowflake.Role('test-role')

# Create a user
user = snowflake.User("py-user", default_role='ORGADMIN')

# Grant privileges to a role
# snowflake.GrantPrivilegesToRole('grant', privileges=[
#                                 'MONITOR'], with_grant_option=False, role_name=role)

grant = snowflake.UserGrant('grant', privilege='MONITOR', roles=[
                    role], user_name=user, with_grant_option=False)

# Export values
pulumi.export("username", user.name)
pulumi.export("role", role)
pulumi.export("grant", grant)