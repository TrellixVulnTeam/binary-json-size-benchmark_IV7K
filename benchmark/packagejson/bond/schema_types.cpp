
//------------------------------------------------------------------------------
// This code was generated by a tool.
//
//   Tool : Bond Compiler 0.12.1.0
//   Input filename:  benchmark/packagejson/bond/schema.bond
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

    
    const ::bond::Metadata Repository::Schema::metadata
        = Repository::Schema::GetMetadata();
    
    const ::bond::Metadata Repository::Schema::s_type_metadata
        = ::bond::reflection::MetadataInit("type", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Repository::Schema::s_url_metadata
        = ::bond::reflection::MetadataInit("url", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());

    
    const ::bond::Metadata Bugs::Schema::metadata
        = Bugs::Schema::GetMetadata();
    
    const ::bond::Metadata Bugs::Schema::s_url_metadata
        = ::bond::reflection::MetadataInit("url", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());

    
    const ::bond::Metadata License::Schema::metadata
        = License::Schema::GetMetadata();
    
    const ::bond::Metadata License::Schema::s_type_metadata
        = ::bond::reflection::MetadataInit("type", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata License::Schema::s_url_metadata
        = ::bond::reflection::MetadataInit("url", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());

    
    const ::bond::Metadata Scripts::Schema::metadata
        = Scripts::Schema::GetMetadata();
    
    const ::bond::Metadata Scripts::Schema::s_test_metadata
        = ::bond::reflection::MetadataInit("test", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());

    
    const ::bond::Metadata Engines::Schema::metadata
        = Engines::Schema::GetMetadata();
    
    const ::bond::Metadata Engines::Schema::s_node_metadata
        = ::bond::reflection::MetadataInit("node", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());

    
    const ::bond::Metadata Dependencies::Schema::metadata
        = Dependencies::Schema::GetMetadata();
    
    const ::bond::Metadata Dependencies::Schema::s_async_metadata
        = ::bond::reflection::MetadataInit("async", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Dependencies::Schema::s_coffeeScript_metadata
        = ::bond::reflection::MetadataInit("coffeeScript", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Dependencies::Schema::s_colors_metadata
        = ::bond::reflection::MetadataInit("colors", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Dependencies::Schema::s_dateformat_metadata
        = ::bond::reflection::MetadataInit("dateformat", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Dependencies::Schema::s_eventemitter2_metadata
        = ::bond::reflection::MetadataInit("eventemitter2", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Dependencies::Schema::s_findupSync_metadata
        = ::bond::reflection::MetadataInit("findupSync", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Dependencies::Schema::s_glob_metadata
        = ::bond::reflection::MetadataInit("glob", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Dependencies::Schema::s_hooker_metadata
        = ::bond::reflection::MetadataInit("hooker", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Dependencies::Schema::s_iconvLite_metadata
        = ::bond::reflection::MetadataInit("iconvLite", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Dependencies::Schema::s_minimatch_metadata
        = ::bond::reflection::MetadataInit("minimatch", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Dependencies::Schema::s_nopt_metadata
        = ::bond::reflection::MetadataInit("nopt", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Dependencies::Schema::s_rimraf_metadata
        = ::bond::reflection::MetadataInit("rimraf", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Dependencies::Schema::s_lodash_metadata
        = ::bond::reflection::MetadataInit("lodash", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Dependencies::Schema::s_underscoreString_metadata
        = ::bond::reflection::MetadataInit("underscoreString", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Dependencies::Schema::s_which_metadata
        = ::bond::reflection::MetadataInit("which", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Dependencies::Schema::s_jsYaml_metadata
        = ::bond::reflection::MetadataInit("jsYaml", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Dependencies::Schema::s_exit_metadata
        = ::bond::reflection::MetadataInit("exit", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Dependencies::Schema::s_getobject_metadata
        = ::bond::reflection::MetadataInit("getobject", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Dependencies::Schema::s_gruntLegacyUtil_metadata
        = ::bond::reflection::MetadataInit("gruntLegacyUtil", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Dependencies::Schema::s_gruntLegacyLog_metadata
        = ::bond::reflection::MetadataInit("gruntLegacyLog", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());

    
    const ::bond::Metadata DevDependencies::Schema::metadata
        = DevDependencies::Schema::GetMetadata();
    
    const ::bond::Metadata DevDependencies::Schema::s_temporary_metadata
        = ::bond::reflection::MetadataInit("temporary", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata DevDependencies::Schema::s_gruntContribJshint_metadata
        = ::bond::reflection::MetadataInit("gruntContribJshint", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata DevDependencies::Schema::s_gruntContribNodeunit_metadata
        = ::bond::reflection::MetadataInit("gruntContribNodeunit", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata DevDependencies::Schema::s_gruntContribWatch_metadata
        = ::bond::reflection::MetadataInit("gruntContribWatch", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata DevDependencies::Schema::s_difflet_metadata
        = ::bond::reflection::MetadataInit("difflet", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata DevDependencies::Schema::s_semver_metadata
        = ::bond::reflection::MetadataInit("semver", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata DevDependencies::Schema::s_shelljs_metadata
        = ::bond::reflection::MetadataInit("shelljs", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());

    
    const ::bond::Metadata Main::Schema::metadata
        = Main::Schema::GetMetadata();
    
    const ::bond::Metadata Main::Schema::s_name_metadata
        = ::bond::reflection::MetadataInit("name", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Main::Schema::s_description_metadata
        = ::bond::reflection::MetadataInit("description", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Main::Schema::s_version_metadata
        = ::bond::reflection::MetadataInit("version", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Main::Schema::s_author_metadata
        = ::bond::reflection::MetadataInit("author", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Main::Schema::s_homepage_metadata
        = ::bond::reflection::MetadataInit("homepage", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Main::Schema::s_repository_metadata
        = ::bond::reflection::MetadataInit("repository", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Main::Schema::s_bugs_metadata
        = ::bond::reflection::MetadataInit("bugs", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Main::Schema::s_licenses_metadata
        = ::bond::reflection::MetadataInit("licenses", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Main::Schema::s_main_metadata
        = ::bond::reflection::MetadataInit("main", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Main::Schema::s_scripts_metadata
        = ::bond::reflection::MetadataInit("scripts", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Main::Schema::s_engines_metadata
        = ::bond::reflection::MetadataInit("engines", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Main::Schema::s_keywords_metadata
        = ::bond::reflection::MetadataInit("keywords", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Main::Schema::s_dependencies_metadata
        = ::bond::reflection::MetadataInit("dependencies", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Main::Schema::s_devDependencies_metadata
        = ::bond::reflection::MetadataInit("devDependencies", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Main::Schema::s_readme_metadata
        = ::bond::reflection::MetadataInit("readme", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Main::Schema::s__id_metadata
        = ::bond::reflection::MetadataInit("_id", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Main::Schema::s__from_metadata
        = ::bond::reflection::MetadataInit("_from", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());

    
} // namespace benchmark