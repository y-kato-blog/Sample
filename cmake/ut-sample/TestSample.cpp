#include "gtest/gtest.h"

class TestSample : public ::testing::Test {
protected:
    TestSample() {
    }

    virtual ~TestSample() {
    }

    virtual void SetUp() {
    }

    virtual void TearDown() {
    }
};

TEST_F(TestSample, Test1) {
  EXPECT_EQ(0, 0);
}

int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}

