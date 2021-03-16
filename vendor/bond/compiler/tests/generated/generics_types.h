
#pragma once

#include <bond/core/bond_version.h>

#if BOND_VERSION < 0x0902
#error This file was generated by a newer version of the Bond compiler and is incompatible with your version of the Bond library.
#endif

#if BOND_MIN_CODEGEN_VERSION > 0x0c10
#error This file was generated by an older version of the Bond compiler and is incompatible with your version of the Bond library.
#endif

#include <bond/core/config.h>
#include <bond/core/containers.h>
#include <bond/core/nullable.h>


namespace tests
{
    
    template <typename T1, typename T2>
    struct Foo
    {
        T2 t2;
        ::bond::nullable< ::tests::Foo<T1, bool> > n;
        
        Foo()
          : t2()
        {
        }

        
        // Compiler generated copy ctor OK
        Foo(const Foo&) = default;
        
        Foo(Foo&&) = default;
        
        
        // Compiler generated operator= OK
        Foo& operator=(const Foo&) = default;
        Foo& operator=(Foo&&) = default;

        bool operator==(const Foo& other) const
        {
            return true
                && (t2 == other.t2)
                && (n == other.n);
        }

        bool operator!=(const Foo& other) const
        {
            return !(*this == other);
        }

        void swap(Foo& other)
        {
            using std::swap;
            swap(t2, other.t2);
            swap(n, other.n);
        }

        struct Schema;

    protected:
        void InitMetadata(const char*, const char*)
        {
        }
    };

    template <typename T1, typename T2>
    inline void swap(::tests::Foo<T1, T2>& left, ::tests::Foo<T1, T2>& right)
    {
        left.swap(right);
    }
} // namespace tests
