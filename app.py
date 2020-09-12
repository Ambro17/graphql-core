from graphql import (
    GraphQLSchema,
    GraphQLObjectType,
    GraphQLField,
    GraphQLString,
    print_schema,
    print_introspection_schema,
    graphql_sync
)


def resolve_it(*args):
    return 'Hidden'


schema = GraphQLSchema(
    query=GraphQLObjectType(
        name='RootQueryType',
        fields=lambda: {
            'hello': GraphQLField(
                GraphQLString, resolve=lambda obj, info: 'world'
            ),
            'hidden': GraphQLField(
                GraphQLString, resolve=resolve_it, visible=lambda c: False
            ),
        }
    )
)

print(print_schema(schema))  # Bypasses field visibility as it doesn't have a context info
print(graphql_sync(schema, '{hidden}'))
print(graphql_sync(schema, '{ inexistent_field}'))  # We should show this error when fields are invisible
print(graphql_sync(schema, '{ __schema {types {name fields {name}} } }'))
