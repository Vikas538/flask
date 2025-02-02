"""added api_key_id to assistants

Revision ID: fcca14ef2b71
Revises: 47c5ba165ca9
Create Date: 2024-05-28 21:04:29.578701

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fcca14ef2b71'
down_revision = '47c5ba165ca9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('actions', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('api_keys', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('assistants', schema=None) as batch_op:
        batch_op.add_column(sa.Column('api_key_id', sa.Integer(), nullable=True))
        batch_op.create_unique_constraint(None, ['id'])
        batch_op.create_foreign_key(None, 'api_keys', ['api_key_id'], ['id'])

    with op.batch_alter_table('base_plan', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('company', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('company_plan', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('conversations', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('customers', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('email_templates', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('invoice', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('knowledge_base', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('module_profile', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('note', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('oauth_detail', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('permissions', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('processed_actions', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('requests', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('role_permission_map', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('sent_email', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('sessions', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('training_data', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('user_meta_data', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('user_plan_usage_balance', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('user_role', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_role', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('user_plan_usage_balance', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('user_meta_data', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('training_data', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('sessions', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('sent_email', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('role_permission_map', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('requests', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('processed_actions', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('permissions', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('oauth_detail', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('note', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('module_profile', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('knowledge_base', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('invoice', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('email_templates', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('customers', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('conversations', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('company_plan', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('company', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('base_plan', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('assistants', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('api_key_id')

    with op.batch_alter_table('api_keys', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('actions', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
