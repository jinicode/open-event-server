"""empty message

Revision ID: abad6f635a43
Revises: 99217a8bc9b2
Create Date: 2020-10-13 16:18:06.702635

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'abad6f635a43'
down_revision = '99217a8bc9b2'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_sessions_version_operation_type', table_name='sessions_version')
    op.drop_index('ix_sessions_version_transaction_id', table_name='sessions_version')
    op.drop_table('sessions_version')
    op.drop_index('ix_speakers_sessions_version_operation_type', table_name='speakers_sessions_version')
    op.drop_index('ix_speakers_sessions_version_transaction_id', table_name='speakers_sessions_version')
    op.drop_table('speakers_sessions_version')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('speakers_sessions_version',
    sa.Column('speaker_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('session_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('transaction_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('operation_type', sa.SMALLINT(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('transaction_id', name='speakers_sessions_version_pkey')
    )
    op.create_index('ix_speakers_sessions_version_transaction_id', 'speakers_sessions_version', ['transaction_id'], unique=False)
    op.create_index('ix_speakers_sessions_version_operation_type', 'speakers_sessions_version', ['operation_type'], unique=False)
    op.create_table('sessions_version',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('subtitle', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('short_abstract', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('long_abstract', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('comments', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('starts_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('ends_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('track_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('language', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('microlocation_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('session_type_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('slides_url', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('video_url', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('audio_url', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('signup_url', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('event_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('state', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('deleted_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('submitted_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('submission_modifier', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('is_mail_sent', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('transaction_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('operation_type', sa.SMALLINT(), autoincrement=False, nullable=False),
    sa.Column('level', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('creator_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('last_modified_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('send_email', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('is_locked', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=False),
    sa.Column('complex_field_values', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', 'transaction_id', name='session_version_pkey')
    )
    op.create_index('ix_sessions_version_transaction_id', 'sessions_version', ['transaction_id'], unique=False)
    op.create_index('ix_sessions_version_operation_type', 'sessions_version', ['operation_type'], unique=False)
    # ### end Alembic commands ###
