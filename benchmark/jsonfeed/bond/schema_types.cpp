
//------------------------------------------------------------------------------
// This code was generated by a tool.
//
//   Tool : Bond Compiler 0.12.1.0
//   Input filename:  benchmark/jsonfeed/bond/schema.bond
//   Output filename: schema_types.cpp
//
// Changes to this file may cause incorrect behavior and will be lost when
// the code is regenerated.
// <auto-generated />
//------------------------------------------------------------------------------

#include "schema_reflection.h"
#include <bond/core/exception.h>

namespace benchmark
{
    
    const ::bond::Metadata Author::Schema::metadata
        = Author::Schema::GetMetadata();
    
    const ::bond::Metadata Author::Schema::s_name_metadata
        = ::bond::reflection::MetadataInit("name", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Author::Schema::s_url_metadata
        = ::bond::reflection::MetadataInit("url", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Author::Schema::s_avatar_metadata
        = ::bond::reflection::MetadataInit("avatar", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());

    
    const ::bond::Metadata Item::Schema::metadata
        = Item::Schema::GetMetadata();
    
    const ::bond::Metadata Item::Schema::s_id_metadata
        = ::bond::reflection::MetadataInit("id", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Item::Schema::s_url_metadata
        = ::bond::reflection::MetadataInit("url", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Item::Schema::s_content_text_metadata
        = ::bond::reflection::MetadataInit("content_text", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Item::Schema::s_date_published_metadata
        = ::bond::reflection::MetadataInit("date_published", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());

    
    const ::bond::Metadata Main::Schema::metadata
        = Main::Schema::GetMetadata();
    
    const ::bond::Metadata Main::Schema::s_version_metadata
        = ::bond::reflection::MetadataInit("version", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Main::Schema::s_user_comment_metadata
        = ::bond::reflection::MetadataInit("user_comment", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Main::Schema::s_title_metadata
        = ::bond::reflection::MetadataInit("title", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Main::Schema::s_home_page_url_metadata
        = ::bond::reflection::MetadataInit("home_page_url", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Main::Schema::s_feed_url_metadata
        = ::bond::reflection::MetadataInit("feed_url", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Main::Schema::s_author_metadata
        = ::bond::reflection::MetadataInit("author", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Main::Schema::s_items_metadata
        = ::bond::reflection::MetadataInit("items", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());

    
} // namespace benchmark
