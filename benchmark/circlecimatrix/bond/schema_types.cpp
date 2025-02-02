
//------------------------------------------------------------------------------
// This code was generated by a tool.
//
//   Tool : Bond Compiler 0.12.1.0
//   Input filename:  benchmark/circlecimatrix/bond/schema.bond
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
    
    const ::bond::Metadata Parameters::Schema::metadata
        = Parameters::Schema::GetMetadata();
    
    const ::bond::Metadata Parameters::Schema::s_a_metadata
        = ::bond::reflection::MetadataInit("a", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());

    
    const ::bond::Metadata Matrix::Schema::metadata
        = Matrix::Schema::GetMetadata();
    
    const ::bond::Metadata Matrix::Schema::s_parameters_metadata
        = ::bond::reflection::MetadataInit("parameters", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());

    
    const ::bond::Metadata M1::Schema::metadata
        = M1::Schema::GetMetadata();
    
    const ::bond::Metadata M1::Schema::s_matrix_metadata
        = ::bond::reflection::MetadataInit("matrix", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());

    
    const ::bond::Metadata Job::Schema::metadata
        = Job::Schema::GetMetadata();
    
    const ::bond::Metadata Job::Schema::s_m1_metadata
        = ::bond::reflection::MetadataInit("m1", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());

    
    const ::bond::Metadata TestWorkflow::Schema::metadata
        = TestWorkflow::Schema::GetMetadata();
    
    const ::bond::Metadata TestWorkflow::Schema::s_jobs_metadata
        = ::bond::reflection::MetadataInit("jobs", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());

    
    const ::bond::Metadata Workflows::Schema::metadata
        = Workflows::Schema::GetMetadata();
    
    const ::bond::Metadata Workflows::Schema::s_test_metadata
        = ::bond::reflection::MetadataInit("test", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());

    
    const ::bond::Metadata Main::Schema::metadata
        = Main::Schema::GetMetadata();
    
    const ::bond::Metadata Main::Schema::s_version_metadata
        = ::bond::reflection::MetadataInit("version", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());
    
    const ::bond::Metadata Main::Schema::s_workflows_metadata
        = ::bond::reflection::MetadataInit("workflows", ::bond::reflection::required_field_modifier::value,
                ::bond::reflection::Attributes());

    
} // namespace benchmark
