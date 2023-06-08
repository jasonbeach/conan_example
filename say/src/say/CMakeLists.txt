
target_sources(say
  PRIVATE
    say.cpp
)

install(
  FILES 
    say.h

  DESTINATION
    ${PROJECT_INSTALL_INCLUDE_DIR}
)